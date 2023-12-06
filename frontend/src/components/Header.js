import React from 'react';
import { Navbar, Container } from 'react-bootstrap';
import { ReactComponent as Logo } from '../images/logo.svg';

const style = {
  backgroundColor: '#fff',
};

export default function Header({ title }) {
  return (
    <Navbar style={style} data-bs-theme="light">
      <Container>
        <Logo style={{ maxWidth: '20rem', maxHeight: '4rem' }} />
      </Container>
    </Navbar>
  );
}
