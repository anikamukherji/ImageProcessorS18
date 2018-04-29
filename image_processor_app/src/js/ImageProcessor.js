import React, { Component } from 'react';
import ImageView from './ImageView';
import ButtonView from './ButtonView';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import Toggle from 'material-ui/Toggle';
import DefaultImage from '../images/default.jpg';
import axios from 'axios';
import '../css/ImageProcessor.css';

//var hostName = "http://vcm-3576.vm.duke.edu:5000/"
var hostName = "http://127.0.0.1:5000/"

class ImageProcessor extends Component {

  constructor() {
    super()
    this.state = {
      imageUploaded: false,
      imageName: null,
      imageFile: DefaultImage,
      currentImageString: DefaultImage,
      processedImageString: null,
      blackFrameOn: false,
      userPressedButton: false,
      buttonIndexSelected: null,
    }
  }

  onDrop = files => {
    // handler for DropZone upload to update state
    if (files.length > 0) {
      var file = files[0]
      this.setState({
        imageUploaded: true,
        imageName: file.name,
        imageFile: file,
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
    }) 
    this.processImage()
  }

  processImage = () => {
    var dict = {
      "username": this.props.username,
      "image": this.state.currentImageString,
    }
    var requestURL;
    switch(this.state.buttonIndexSelected){
      case 0: 
        requestURL = hostName + "api/histogram_equalization"
        break
      //case 1: 
        //requestURL = hostName + "api/contrast_stretching"
        //break
      //case 2: 
        //requestURL = hostName + "api/log_compression"
        //break
      //case 3: 
        //requestURL = hostName + "api/reverse_video"
        //break
      default:
        return
    } 
    console.log("starting request")
    axios.post(requestURL, dict).then( response => { 
      console.log(response)
      var data = response.data
      var b64string = data.base64
      let base64Image = b64string.split('b\'').pop();
      base64Image = "data:image/png;base64," + base64Image

      this.setState({
        processedImageString: base64Image,
        userPressedButton: true,
      });
      console.log("finished request")
      console.log(this.state.processedImageString)
      console.log(this.state.currentImageString)
    });
  }

  render() {
    return (
      <div className="container">
        <MuiThemeProvider muiTheme={muiTheme}>
          <p className="basic-text"> Welcome {this.props.username}! </p>
          <p className="basic-text"> Click on the image on the left to upload your own </p>
          <div className="image-container">
            <ImageView 
              currentImageString={this.state.currentImageString} 
              processedImageString={this.state.processedImageString} 
              onDrop={this.onDrop} 
              imageUploaded={this.state.imageUploaded} 
              blackFrameOn={this.state.blackFrameOn} 
              userHasProcessedImage={this.state.userPressedButton}
            />
          </div>

            <div className="toggle">
              <Toggle
                label="Black Frame"
                onToggle={this.onFrameToggle}
                labelStyle={{ fontFamily: 'Raleway, sans-serif' }}
              />
            </div>

          <ButtonView onClickParentCallback={this.onClick}/>
        </MuiThemeProvider>

        <p className="footer-text"> Default Photo: Photo by Dylan Gialanella on Unsplash</p>
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
