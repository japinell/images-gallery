import React from 'react';
import { Navbar, Container } from 'react-bootstrap';

const style = {
  backgroundColor: 'lightblue',
};

export default function Header({ title }) {
  return (
    <Navbar style={style} data-bs-theme="light">
      <Container>
        <Navbar.Brand href="/">{title}</Navbar.Brand>
      </Container>
    </Navbar>
  );
}
