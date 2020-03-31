import { Route, Switch } from "react-router-dom"
import React from "react"
import NoMatch from "views/NoMatch"
import Home from "views/Home"
import PhotoSelect from "views/PhotoSelect"
import Store from "views/Store"
import CompanyPage from "views/CompanyPage"
import Map from "components/Map/Map"
import OrderForm from "../views/OrderForm";

// Placeholders for now
// use the route for the HomeView as reference for all others
// eg: <Route path="/my-view" component={MyView} />
function Routes() {
  return (
    <Switch>
      <Route exact path="/stores">
        <h2>Insert stores list/map</h2>
      </Route>
      <Route exact path="/stores/:id" component={Store} />
      <Route exact path="/company" component={CompanyPage} />
      <Route path="/company/photo-select" component={PhotoSelect} />
      <Route path="/order/:step" component={OrderForm} />
      <Route path="/map" component={Map} />
      <Route exact path="/" component={Home} />
      <Route component={NoMatch} />
    </Switch>
  )
}

export default Routes
