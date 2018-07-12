import React from 'react';
import {render} from 'react-dom';
import Main from './components/Main';

const mountApp = document.getElementById('app');

mountApp && render(<Main />, mountApp);