import React from 'react';
import { Spinner as Loader } from 'react-bootstrap';

const spinnerStyle = {
  position: 'absolute',
  top: 'calc(50% - 1rem)',
  left: 'calc(50% - 1rem)',
};

export default function Spinner() {
  return (
    <Loader
      style={spinnerStyle}
      animation="border"
      role="status"
      variant="primary"
    >
      <span className="visually-hidden">Loading...</span>
    </Loader>
  );
}
