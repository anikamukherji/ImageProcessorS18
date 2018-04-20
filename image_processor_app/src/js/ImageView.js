import React, { Component } from 'react';
import Dropzone from 'react-dropzone'
import '../css/ImageView.css';

class ImageView extends Component {

  renderProcessedImage = () => {
    
    if (this.props.userHasProcessedImage) {
      return (
        <img className="selected-image" src={this.props.image} alt="Selected"/>
      ) 
    }
  }

  render() {

    var frameStyle = {
      backgroundColor: this.props.blackFrameOn ? "black" : "white",
      height: 250,
      padding: 25,
    }

    return (
      <div className="image-view" style={frameStyle}>
        <div className="dropzone">
         <Dropzone
            accept="image/jpeg, image/jpg, image/png"
            onDrop={this.props.onDrop}
            style={{ backgroundColor: "clear" }}
          >
          <img className="selected-image" src={this.props.image} alt="Selected"/>
          </Dropzone>
        </div>
        <div className="dropzone">
          {this.renderProcessedImage()}
        </div>
      </div>
    );
  }
}

export default ImageView;
