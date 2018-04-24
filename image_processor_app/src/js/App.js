import React, { Component } from 'react';
import '../css/App.css';
import ImageView from './ImageView';
import ButtonView from './ButtonView';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import Toggle from 'material-ui/Toggle';
import TextField from 'material-ui/TextField';
import DefaultImage from '../images/default.jpg';

class App extends Component {

  constructor() {
    super()
    this.state = {
      currUser: null,
      imageUploaded: false,
      imageName: null,
      imageFile: DefaultImage,
      currentImageString: DefaultImage,
      processedImageString: DefaultImage,
      blackFrameOn: false,
      userPressedButton: false,
      buttonIndexSelected: null,
    }
  }

  handleChange = event => {
    // handler for username textbox
    this.setState({
      currUser: event.target.value
    });
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
      {"curr_user": this.state.currUser,
        "image_uploaded": this.state.currentImageString,
        "time_stamp": Date.now(),
      }
    return dict
  }

  prepFile = file => {
    // convert image to base64 and save in state
    const reader = new FileReader();
    reader.readAsDataURL(file);
    console.log(file.naturalHeight)
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
    // TO DO
    // Based on index, call specific handler to make
    // request to server
    // Update self.state.processedImageString based on response
    this.setState({
      buttonIndexSelected: index,
      userPressedButton: true,
    }) 
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Image Processor</h1>
        </header>

        <MuiThemeProvider muiTheme={muiTheme}>

        <TextField
            hintText="Username"
            onChange={this.handleChange} 
            underlineFocusStyle={{borderColor: '#440014'}}
        />

        <p className="basic-text"> Click on the image on the left to upload your own </p>

        <div className="image-container">
          <ImageView imageString={this.state.currentImageString} onDrop={this.onDrop} imageUploaded={this.state.imageUploaded} blackFrameOn={this.state.blackFrameOn} userHasProcessedImage={this.state.userPressedButton}/>
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

export default App;
