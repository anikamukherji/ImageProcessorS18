import React, { Component } from 'react';
import Dropzone from 'react-dropzone'
import '../css/ImageView.css';

class ImageView extends Component {

  render() {

    var frameStyle = {
      backgroundColor: this.props.blackFrameOn ? "black" : "white",
      height: 250,
      width: 200,
      padding: 25,
    }

    return (
      <div className="image-view">
        <div className="dropzone">
         <Dropzone
            accept="image/jpeg, image/jpg, image/png"
            onDrop={this.props.onDrop}
            style={frameStyle}
          >
          <img className="selected-image" src={this.props.image} alt="Selected"/>
          </Dropzone>
        </div>
      </div>
    );
  }
}

export default ImageView;
