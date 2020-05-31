import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TimelapseComponent } from './timelapse/timelapse.component';
import { MainPageComponent } from './main-page/main-page.component';

const routes: Routes = [
  { path: 'timelapse', component: TimelapseComponent},
  { path: 'mainpage', component: MainPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }