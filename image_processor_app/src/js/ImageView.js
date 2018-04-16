import React, { Component } from 'react';
import Dropzone from 'react-dropzone'
import '../css/ImageView.css';

class ImageView extends Component {

  constructor() {
    super()
    this.state = {
      imageUploaded: false,
      imageName: null,
      image: null,
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

  render() {
    return (
      <div className="image-view">
        <div className="dropzone">
         <Dropzone
              accept="image/jpeg, image/jpg, image/png"
              onDrop={ this.onDrop }
          >
          <img className="selected-image" src={this.state.image} alt="Selected"/>
          </Dropzone>
        </div>
      </div>
    );
  }
}

export default ImageView;
