import React, { Component } from 'react';
import RaisedButton from 'material-ui/RaisedButton';

class ButtonView extends Component {

  buttonPressed = tag => {
    this.props.onClickParentCallback(tag)
  }

  render() {
    const style = {
      margin: 12,
    };

    return (
      <div className="button-container">
        <RaisedButton label="Histogram Equalization" style={style} onClick={ () => this.buttonPressed(0) }/>
        <RaisedButton label="Contrast Stretching" style={style} onClick={ () => this.buttonPressed(1) }/>
        <RaisedButton label="Log Compression" style={style} onClick={ () => this.buttonPressed(2) }/>
        <RaisedButton label="Reverse Video" style={style} onClick={ () => this.buttonPressed(3) }/>
      </div>
    );
  }
}

export default ButtonView;
