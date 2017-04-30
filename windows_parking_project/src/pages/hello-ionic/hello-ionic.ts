import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {Http} from '@angular/http';
import 'rxjs/Rx';

/** This is where data is being sent to the html page **/

@Component({
  selector: 'page-hello-ionic',
  templateUrl: 'hello-ionic.html'
})
export class HelloIonicPage {
  data:any
  constructor(public navCtrl: NavController,http:Http) {
     var response = http.get("http://localhost:1337/")
     .map((res) =>res.json())
     .subscribe((data)=>{
     this.data = data;
     console.log(response);
   })
  }
}