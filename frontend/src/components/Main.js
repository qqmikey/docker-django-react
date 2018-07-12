import React, {Component} from 'react';
import {hot} from 'react-hot-loader';

class Main extends Component {

    constructor(props, context) {
        super(props, context);
        // let data = JSON.parse(document.getElementById('app').dataset.json);
        this.state = {};
    }

    componentDidMount() { }

    render() {
        return (
            <h1>react!</h1>
        );
    }

}

export default hot(module)(Main);