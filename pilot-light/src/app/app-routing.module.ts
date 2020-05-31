import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TimelapseComponent } from './timelapse/timelapse.component';
import { AppComponent } from './app.component';

const routes: Routes = [
  { path: 'app-timelapse', component: TimelapseComponent, pathMatch: 'full'},
  { path: 'app-main-page', component: AppComponent, pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }