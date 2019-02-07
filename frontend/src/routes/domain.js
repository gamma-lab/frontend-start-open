import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Route, Switch, Redirect } from 'react-router-dom';
// import { setCurrentDomain as actionSetCurrentDomain } from 'Redux/domains/actions';
// import { connect } from 'react-redux';

// import Dashboard from './domains/dashboard';
// import Stories from './stories';
// import Actions from './actions';
// import Intents from './intents';
import TableList from 'views/TableList/TableList.jsx';
import UpgradeToPro from 'views/UpgradeToPro/UpgradeToPro.jsx';
import DomainList from 'views/Domain/DomainList';

class DomainRouter extends Component {
  // handleSetCurrentDomain (domainID) {
  //   if (domainID !== this.props.currentDomainID) {
  //     this.props.setCurrentDomain(domainID);
  //   }
  // }

  render() {
    const { match } = this.props;
    // const {
    //   setCurrentDomain,
    //   match,
    //   match: {
    //     params: { domainID }
    //   },
    //   currentDomainID
    // } = this.props;
    // if (currentDomainID !== domainID) setCurrentDomain(domainID);
    // const matches = this.props.location.pathname.match(/\/domain\/(.*)/);
    // if (matches.length === 2 && matches[1] && matches[1] !== currentDomainID) {
    //   this.props.setCurrentDomain(matches[1]);
    // }
    return (
      <Switch>
        {/*<Route path={`${match.url}/stories`} component={Stories} />
        <Route path={`${match.url}/actions`} component={Actions} />
        <Route path={`${match.url}/intents`} component={Intents} />*/}
        <Route exact path={`${match.url}`} component={DomainList} />
        <Route path={`${match.url}/:domainID`} component={UpgradeToPro} />
        <Redirect to="/error/404" />
      </Switch>
    );
  }
}

// const mapDispatchToProps = function (dispatch) {
//   return {
//     setCurrentDomain: (id, history = null) => {
//       dispatch(actionSetCurrentDomain(id, history));
//     }
//   };
// };
//
// const mapStateToProps = state => ({
//   currentDomainID: state.domains.currentDomain
//     ? state.domains.currentDomain._id
//     : undefined
// });

DomainRouter.propTypes = {
  match: PropTypes.shape({
    url: PropTypes.string.isRequired
  }),
  history: PropTypes.object,
  location: PropTypes.object,
  setCurrentDomain: PropTypes.func,
  currentDomainID: PropTypes.string
};
export default DomainRouter;

// export default withRouter(
//   connect(
//     mapStateToProps,
//     mapDispatchToProps
//   )(DomainRouter)
// );
