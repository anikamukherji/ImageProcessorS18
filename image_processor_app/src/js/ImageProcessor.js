import React, { Component } from 'react';
import ImageView from './ImageView';
import ButtonView from './ButtonView';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import Toggle from 'material-ui/Toggle';
import DefaultImage from '../images/default.jpg';
import axios from 'axios';
import '../css/ImageProcessor.css';
import '../css/App.css';

var hostName = "http://vcm-3576.vm.duke.edu:5000/"

class ImageProcessor extends Component {

  constructor() {
    super()
    this.state = {
      imageUploaded: false,
      imageName: null,
      imageFile: DefaultImage,
      currentImageString: DefaultImage,
      currentImageType: 'jpg',
      processedImageString: null,
      processedImageReceived: false,
      blackFrameOn: false,
      userPressedButton: false,
      buttonIndexSelected: null,
      processCount: null,
      lastProcessTime: null,
      imageHeight: null,
      imageWidth: null,
    }
  }

  onDrop = files => {
    // handler for DropZone upload to update state
    if (files.length > 0) {
      var file = files[0]
      var fileType = file.type
      fileType = fileType.split('image/').pop()
      this.setState({
        imageUploaded: true,
        imageName: file.name,
        imageFile: file,
        currentImageType: fileType,
      });
      this.prepFile(file);
    }
  }

  userDict = () => {
    var dict = 
      {"curr_user": this.props.username,
        "image_uploaded": this.state.currentImageString,
        "time_stamp": Date.now(),
      }
    return dict
  }

  prepFile = file => {
    // convert image to base64 and save in state
    const reader = new FileReader();
    reader.readAsDataURL(file);
		reader.onloadend = () => {
			this.setState({
        currentImageString: reader.result
      });
		}
  }

  onFrameToggle = () => {
    // switch between white and  black frame
      this.setState({
        blackFrameOn: !this.state.blackFrameOn,
      });
  }

  onClick = index => {
    // keep track of what button has been pressed
    this.setState({
      buttonIndexSelected: index,
      userPressedButton: true,
    }) 
    this.processImage(index)
  }

  processImage = index => {
    var dict = {
      "username": this.props.username,
      "image": this.state.currentImageString,
      "file_type": this.state.currentImageType,
    }
    var requestURL;
    switch(index){
      case 0: 
        requestURL = hostName + "api/histogram_equalization"
        break
      case 1: 
        requestURL = hostName + "api/contrast_stretching"
        break
      case 2: 
        requestURL = hostName + "api/log_compression"
        break
      case 3: 
        requestURL = hostName + "api/reverse_video"
        break
      default:
        return
    } 
    axios.post(requestURL, dict).then( response => { 
      var data = response.data
      var b64string = data.base64
      let base64Image = b64string.split('b\'').pop();
      base64Image = base64Image.slice(0, base64Image.length-3)
      base64Image = "data:image/png;base64," + base64Image

      this.setState({
        processedImageString: base64Image,
        processCount: data.process_count,
        lastProcessTime: data.process_time,
        imageHeight: data.image_size[1],
        imageWidth: data.image_size[0],
        processedImageReceived: true,
      });
    });
  }

  renderStats = () => {
    if (this.state.userPressedButton) {
      if (this.state.processedImageReceived) {
        if (this.props.username !== "Visitor") {
          return (
            <div className="stats">
              The image size has width {this.state.imageWidth} and height {this.state.imageHeight}
                <br/>
              You have performed this action {this.state.processCount} times!
                <br/>
              The last processing took {this.state.lastProcessTime} to complete
            </div>
          )
        } else {
          return (
            <div className="stats">
              The image size has width {this.state.imageWidth} and height {this.state.imageHeight}
                <br/>
              The last processing took {this.state.lastProcessTime} to complete
            </div>
          )
        }
      } else {
        return (
          <div className="stats">
            Image is processing - please be patient!
          </div>
        )
      } 
    }
  }

  render() {
    return (
      <div className="container">
        <MuiThemeProvider muiTheme={muiTheme}>
          <p className="basic-text"> Welcome {this.props.username}! </p>
          <p className="basic-text"> Click on the image to upload your own </p>
            <div className="toggle">
              <Toggle
                label="Black Frame"
                onToggle={this.onFrameToggle}
                labelStyle={{ fontFamily: 'Raleway, sans-serif' }}
              />
            </div>

          <div className="image-container">
            <ImageView 
              currentImageString={this.state.currentImageString} 
              processedImageString={this.state.processedImageString} 
              onDrop={this.onDrop} 
              imageUploaded={this.state.imageUploaded} 
              blackFrameOn={this.state.blackFrameOn} 
              userHasProcessedImage={this.state.userPressedButton}
              processedImageReceived={this.state.processedImageReceived}
            />
          </div>

          {this.renderStats()}

          <ButtonView onClickParentCallback={this.onClick}/>
        </MuiThemeProvider>

        <div className="footer-text">
          <p> Default Photo: Photo by Dylan Gialanella on Unsplash</p>
          <p> BME590 Final Project </p>
          <p> Anika Mukherji </p>
          <p> Zhiwei Kang </p>
          <p> Yi Zhao </p>
        </div>
      </div>
    );
  }
}

const muiTheme = getMuiTheme({
  toggle: {
    thumbOnColor: '#440014',
    trackOnColor: '#daf0ee',
  },
});

export default ImageProcessor;
