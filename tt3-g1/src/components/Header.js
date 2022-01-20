// import React from 'react';
import PropTypes from 'prop-types';
import Button from './Button'

const Header = ({title}) => {
  return (
    <header className='Header'>
      <h1 style={headingStyle}>{title}</h1>
      <Button color='red' text='Create Post'/>
      </header>
  )
}

Header.defaultProps = {
    title: 'Task Tracker'
}

Header.propTypes = {
    title: PropTypes.string.isRequired,
}

const headingStyle = {
    color: 'black', 
    backgroundColor: ''
}

export default Header;
