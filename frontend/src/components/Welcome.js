import React from 'react';
import { Button } from 'react-bootstrap';

export default function Welcome() {
  return (
    <div>
      <h1>Images Gallery</h1>
      <p>
        This is a simple application that retrieves photos from unsplash.com.
      </p>
      <p>
        <Button variant="primary" href="https://unsplash.com" target="_blank">
          Learn more
        </Button>
      </p>
    </div>
  );
}
