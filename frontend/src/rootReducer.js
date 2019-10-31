import { combineReducers } from 'redux';

import * as appReducers from './app/appReducers';


const rootReducer = history => combineReducers({
  ...appReducers,
  // ... rest of your reducers
});

export default rootReducer;
