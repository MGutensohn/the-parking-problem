import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {Http} from '@angular/http';
import 'rxjs/Rx';


@Component({
  selector: 'page-hello-ionic',
  templateUrl: 'hello-ionic.html'
})
export class HelloIonicPage {
  data:any
  constructor(public navCtrl: NavController,http:Http) {
     var response = http.get("https://theparkingproblem.appspot.com/")
     .map((res) =>res.json())
     .subscribe((data)=>{
     this.data = data;
     console.log(response);
   })
  }
}