import React, { Component } from 'react';
import '../css/App.css';
import ImageView from './ImageView';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import Toggle from 'material-ui/Toggle';
import DefaultImage from '../images/default.jpg';

class App extends Component {

  constructor() {
    super()
    this.state = {
      imageUploaded: false,
      imageName: null,
      image: DefaultImage,
      blackFrameOn: false,
    }
  }

  onDrop = files => {
    if (files.length > 0) {
      this.setState({
        imageUploaded: true,
        imageName: files[0].name,
        image: files[0].preview,
      });
    }
  }

  onFrameToggle = () => {
      this.setState({
        blackFrameOn: !this.state.blackFrameOn,
      });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Image Processor</h1>
        </header>

        <p className="basic-text"> Click on the image to upload your own </p>

        <MuiThemeProvider>

        <div className="image-container">
          <ImageView image={this.state.image} onDrop={this.onDrop} imageUploaded={this.state.imageUploaded} blackFrameOn={this.state.blackFrameOn}/>
        </div>

          <div className="toggle">
            <Toggle
              label="Black Frame"
              labelPosition="right"
              labelStyle={toggleStyle.toggle}
              onToggle={this.onFrameToggle}
            />
          </div>
        </MuiThemeProvider>

        <p className="basic-text"> Default Photo: Photo by Dylan Gialanella on Unsplash</p>
      </div>
    );
  }
}

const toggleStyle = {
  toggle: {
    marginBottom: 16,
    fontFamily: 'Raleway, sans-serif',
  },
}

export default App;
