/* eslint-disable prefer-destructuring */
import React from 'react';
import { render } from 'react-dom';
import DevTools from './DevTools';

const usePopup = false;

export default function showDevTools(store) {
  let document;
  if (usePopup) {
    const popup = window.open(null, 'Redux DevTools', 'menubar=no,location=no,resizable=yes,scrollbars=no,status=no');
    // Reload in case it already exists
    popup.location.reload();
    document = popup.document;
  } else {
    document = window.document;
  }

  setTimeout(() => {
    const id = 'react-devtools-root';
    if (!usePopup) {
      const elem = document.createElement('div');
      elem.setAttribute('id', id);
      document.body.appendChild(elem);
    } else document.write(`<div id="${id}"></div>`);
    render(
      <DevTools store={store} />,
      document.getElementById(id)
    );
  }, 10);
}
