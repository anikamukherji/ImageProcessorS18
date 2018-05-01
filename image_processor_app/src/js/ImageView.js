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
      console.log(this.props.currentImageString)    
      console.log(this.props.processedImageString)    
      return (
        <div style={frameStyle}>
          <div className="dropzone">
            <img className="selected-image" id='selImg' src={this.props.processedImageString} alt="None Selected"/>
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
              //accept="image/jpeg, image/jpg, image/png"
              accept="image/png"
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
