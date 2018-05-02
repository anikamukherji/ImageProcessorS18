import React, { Component } from 'react';
import Dropzone from 'react-dropzone'
import '../css/ImageView.css';

class ImageView extends Component {

  renderProcessedImage = () => {

    var frameStyle = {
      backgroundColor: this.props.blackFrameOn ? "black" : "white",
      margin: 25,
    }
    if (this.props.processedImageReceived) {
      return (
        <div className="processed-image-container">
          <div style={frameStyle}>
            <div className="dropzone">
              <a href={this.props.processedImageString} download="image.png">
              <img className="selected-image" id='selImg' src={this.props.processedImageString} alt="None Selected"/>
              </a>
            </div>
          </div>
          <div className="download-container">
            <a className="download-text" href={this.props.processedImageString} download="image"> Download as .png </a>
          </div>
        </div>
      ) 
    }
  }

  render() {

    var frameStyle = {
      backgroundColor: this.props.blackFrameOn ? "black" : "white",
      margin: 25,
    }

    return (
      <div className="image-view">
        <div style={frameStyle}>
          <div className="dropzone">
           <Dropzone
              accept="image/jpeg, image/jpg, image/png"
              onDrop={this.props.onDrop}
              style={{ backgroundColor: "clear" }}
            >
            <img className="selected-image" id='selImg' src={this.props.currentImageString} alt="None Selected"/>
            </Dropzone>
          </div>
        </div>
        {this.renderProcessedImage()}
      </div>
    );
  }
}

export default ImageView;
