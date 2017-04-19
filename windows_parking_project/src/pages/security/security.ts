import { Component } from '@angular/core';



@Component({
  selector: 'page-security',
  templateUrl: 'hello-ionic.html',
  template: `
  	<div [ngStyle]="{'background-image': 'url(' + photo + ')'}"></div>
  	<h3> Admin portal </h3>
  	<button (click)="signIn()">sign-in</button>
  	<div *ngIf="signButton">
  		<form>
  		<label> Username: </label><br />
  		<input type="text" username="username" />
  		<label> </label><br />
  		<label>Password: </label><br />
  		<input type="text" password="password" />
  		<label> </label><br />
  		<button (click)="logIn()">log-in</button>

  		<div *ngIf="logButton">
	  		<form>
	  		<label> Welcome {{username}} </label><br />
   `,
})
export class Security {

	username: string;
	password: string;
	signButton: boolean;
	logButton: boolean;


	constructor(){

	this.username = 'username';
	this.password = 'password';
	this.signButton = false;
	this.logButton = false;
	}

	signIn(){
	this.signButton = true;
	}

	logIn(){
	this.logButton = true;
	}
  
}
