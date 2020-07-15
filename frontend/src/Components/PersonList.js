import React from 'react';
import axios from 'axios';

export default class PersonList extends React.Component{
	state = {
		persons:[],
	}

	componentDidMount(){
		//axios.get('http://127.0.0.1:8000/users/1/?format=json')
		//	.then(res => {
		//		this.setState({persons: res.data});
		//	});
		fetch("http://127.0.0.1:8000/groups/1/?format=json")
		.then(res => res.json())
		.then(res => this.setState({persons: json.results }));
	}

	render(){
		return <ul>{this.state.persons.map(person => {return (<li>{person.username}</li>);})}
		</ul>;
	}
}
