import React from 'react';
import { Link, matchPath } from 'react-router-dom';

import OrderItem from 'components/OrderItem/OrderItem';
import "./Order.scss";
import Tab from 'components/Tab/Tab';
import { useTranslation } from 'react-i18next';

const activeOrderStyle = 'Order-category-item--active';

const Order = (props) => {
  const [t] = useTranslation('order');
  const { location, match } = props;
  const pathMatch = matchPath(location.pathname, { path: '/stores/:id/orders/:orderId' });

  return (
    <div className="Order">
      <div className="Order-category">
        <Link to={`/stores/${match.params.id}/orders`} className={`Order-category-item ${!pathMatch || !pathMatch.params.orderId ? activeOrderStyle : ''}`}>{t('newOrders')}</Link>
        <Link to={`/stores/${match.params.id}/orders/history`} className={`Order-category-item ${pathMatch && pathMatch.params.orderId ? activeOrderStyle : ''}`}>{t('orderHistory')}</Link>
      </div>
      <div className="OrderItems">
        <OrderItem {...props} />
        <OrderItem {...props} />
        <OrderItem {...props} />
        <OrderItem {...props} />
        <OrderItem {...props} />
      </div>
      <Tab />
    </div>
  )
}

export default Order;
