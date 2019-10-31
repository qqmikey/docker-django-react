// @flow
import { type dispatchType } from '../constants/types';
import { CHANGE_ROTATION_DIRECTION, ANOTHER_ACTION_TYPE } from './appActionTypes';


export function changeRotationDirection() {
  return (dispatch: dispatchType, getState: () => {}) => {
    let { rotationDirection } = getState();
    rotationDirection = (rotationDirection + 1) % 2;
    dispatch({
      type: CHANGE_ROTATION_DIRECTION,
      payload: rotationDirection
    });
  };
}

export function anotherAction() {
  return {
    type: ANOTHER_ACTION_TYPE,
    payload: {},
  };
}
