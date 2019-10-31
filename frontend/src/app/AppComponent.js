// @flow
import { hot } from 'react-hot-loader/root';
import React, { PureComponent } from 'react';

import logo from './logo.svg';
import './app.css';


type Props = {
  +rotation: 0 | 1,

  changeRotationDirection: () => void,
};


class App extends PureComponent<Props> {
  changeRotation = () => {
    const { changeRotationDirection } = this.props;
    changeRotationDirection();
  };

  render() {
    const { rotation } = this.props;
    const logoReverse = rotation ? ' reverse' : '';
    return (
      <div
        className="App"
        role="button"
        tabIndex="0"
        onClick={this.changeRotation}
        onKeyUp={this.changeRotation}
      >
        <header className="App-header">
          <div className="App-logo-container">
            <img src={logo} className={`App-logo${logoReverse}`} alt="logo" />
          </div>
          <p>React + Redux + Flow app.</p>
          <p>
            {/* eslint-disable-next-line react/jsx-one-expression-per-line */}
            Edit <code>src/components/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default hot(App);
