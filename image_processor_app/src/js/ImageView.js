import React, { Component } from 'react';
import Dropzone from 'react-dropzone'
import '../css/ImageView.css';

class ImageView extends Component {

  renderProcessedImage = () => {
    
    if (this.props.userHasProcessedImage) {
      return (
        <img className="selected-image" src={this.props.imageString} alt="None Selected"/>
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
            <img className="selected-image" src={this.props.imageString} alt="None Selected"/>
            </Dropzone>
          </div>
        </div>
        <div style={frameStyle}>
          <div className="dropzone">
            {this.renderProcessedImage()}
          </div>
        </div>
      </div>
    );
  }
}

export default ImageView;
