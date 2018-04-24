import React, { Component } from 'react';
import Dropzone from 'react-dropzone'
import '../css/ImageView.css';

class ImageView extends Component {

  renderProcessedImage = () => {

    var frameStyle = {
      backgroundColor: this.props.blackFrameOn ? "black" : "white",
      margin: 25,
    }
    
    if (this.props.userHasProcessedImage) {
      return (
        <div style={frameStyle}>
          <div className="dropzone">
            <img className="selected-image" src={this.props.imageString} alt="None Selected"/>
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
            <img className="selected-image" id='selImg' src={this.props.imageString} alt="None Selected"/>
            </Dropzone>
          </div>
        </div>
        {this.renderProcessedImage()}
      </div>
    );
  }
}

export default ImageView;
