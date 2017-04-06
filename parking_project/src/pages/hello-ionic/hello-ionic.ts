import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {Http} from '@angular/http';

@Component({
  selector: 'page-hello-ionic',
  templateUrl: 'hello-ionic.html'
})
export class HelloIonicPage {
  data:any
  constructor(public navCtrl: NavController,http:Http) {
      http.get("http://localhost:8090")
     .map((res) =>res.json())
     .subscribe((data)=>{
     this.data = JSON.stringify(data);
   })
  }
}
