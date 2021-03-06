import React from 'react';

import gift from '../../assets/gift.svg';

import './Yippey.scss'

const Yippey = ({ text, footer }) => (
  <div className="Yippey">
    <img src={gift} alt="Gift"/>
    <h1>Yippey!</h1>
    <p>{text}</p>
    {footer}
  </div>
)

export default Yippey

