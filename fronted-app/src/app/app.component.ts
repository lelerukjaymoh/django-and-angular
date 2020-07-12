import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend-app';
  constructor(private _http: HttpClient) {
    this.c1.name = "eli"
  }

  c1: Cust = new Cust();
  click1() {
    this.getBooks().subscribe(b => this.c1.name = b.toString())
  }
  click2() {
    this.getAllBooks().subscribe(b => this.c1 = b)
  }

  getAllBooks() {
    return this._http
      .get<Cust>("./getcust") // GET request  
  }
  getBooks() {
    return this._http
      .post("./apitest/", "5") // POST request with argument
  }
}

export class Cust {
  name: string;
  age: number;
  city: string;
}