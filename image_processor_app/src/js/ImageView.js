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

  getImgSize = id => {
    var pic = document.getElementById(id);
    console.log(id)
    //var h = pic.naturalHeight;
    //var w = pic.offsetWidth;
    //console.log(h) 
    //console.log(w) 
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
            {this.getImgSize('selImg')}
            </Dropzone>
          </div>
        </div>
        {this.renderProcessedImage()}
      </div>
    );
  }
}

export default ImageView;
