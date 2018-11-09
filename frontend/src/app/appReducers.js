// @flow
import { actionType } from '../constants/types';
import { CHANGE_ROTATION_DIRECTION } from './appActionTypes';


// eslint-disable-next-line import/prefer-default-export
export function rotationDirection(state = 0, action: actionType) {
  switch (action.type) {
    case CHANGE_ROTATION_DIRECTION:
      return action.payload;
    default:
      return state;
  }
}
