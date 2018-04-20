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
      image: DefaultImage,
      blackFrameOn: false,
      userPressedButton: true,
      buttonIndexSelected: null,
    }
  }

  handleChange = event => {
    this.setState({
      currUser: event.target.value
    });
  }

  onDrop = files => {
    if (files.length > 0) {
      this.setState({
        imageUploaded: true,
        imageName: files[0].name,
        image: files[0].preview,
      });
    }
    this.prepFile(files[0]);
  }

  prepFile = file => {
    const reader = new FileReader();
    reader.onabort = () => console.log('file reading was aborted');
    reader.onerror = () => console.log('file reading has failed');
    reader.readAsDataURL(file);
    // base64 image stored in reader.result
    console.log(reader)
  }

  onFrameToggle = () => {
      this.setState({
        blackFrameOn: !this.state.blackFrameOn,
      });
  }

  onClick = index => {
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
          <ImageView image={this.state.image} onDrop={this.onDrop} imageUploaded={this.state.imageUploaded} blackFrameOn={this.state.blackFrameOn} userHasProcessedImage={this.state.userPressedButton}/>
        </div>

          <div className="toggle">
            <Toggle
              label="Black Frame"
              labelPosition="right"
              onToggle={this.onFrameToggle}
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
    fontFamily: 'Raleway, sans-serif',
  },
});

export default App;
