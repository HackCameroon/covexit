import { useEffect, useReducer } from 'react'
import axios from 'axios';
import constate from 'constate'
import logger from './Logger'
import useLocalStorage from '../shared/useLocalStorage'


const initialState = {
  selectedLocation: {},
  coordinates: []
};


const reducer = (originalState, action) => {
  let state = Object.assign({}, originalState);
  switch (action.type) {
    case 'SET_SELECTED_COORDINATES':
      return {
        ...state,
        coordinates: action.payload.coordinates,
        selectedLocation: {},
      }

    case 'SET_SELECTED_LOCATION': 
      const { suggestion, coordinates } = action.payload;
      return {
        ...state,
        selectedLocation: suggestion,
        coordinates,
      };

    default: {
      return state;
    }
  }

};

const loggerReducer = logger(reducer);

const useCurrentLocation = () => {
  //  TODO: loader status: 
  // const [isGettingLocation, setIsGettingLocation] = useState(false);
  const [data, setData] = useLocalStorage('locationData', initialState)
  const [state, dispatch] = useReducer(loggerReducer, data)


  useEffect(() => {
    setData(state)
  }, [state, setData])

  const { selectedLocation, coordinates } = state

  const addCoordinates = coordinates => {
    dispatch({
      type: 'SET_SELECTED_COORDINATES',
      payload: { coordinates }
    })
  }

  const addCurrentLocation = () => {
    if (navigator.geolocation) {
      // TODO: loader status: setIsGettingLocation(true);
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const lattitude = position.coords.latitude;
          const longitude = position.coords.longitude;
          const coordinates = [longitude, lattitude];
          // TODO: loader status: setIsGettingLocation(false);
          addCoordinates(coordinates);
        },
        () =>
          setIsGettingLocation(false)
      );
    } else {
      // Browser doesn't support Geolocation
      axios.get('https://ipapi.co/json/')
      .then((response) => {
        const { latitude, longitude } = response;
        const coordinates = [longitude, latitude];
        addCoordinates(coordinates);
      })
      .catch(() => {
        // TODO: loader status: setIsGettingLocation(false);
        console.log('the geolocation service is not supported in your browser');
      });
    }
  };

  const addGoogleLocation = (suggestion, coordinates) => {
    dispatch({
      type: 'SET_SELECTED_LOCATION',
      payload: {suggestion, coordinates}
    })
  }

  return { selectedLocation, coordinates, addCurrentLocation, addGoogleLocation }
};

export const [LocationProvider, useLocationContext] = constate(useCurrentLocation);
