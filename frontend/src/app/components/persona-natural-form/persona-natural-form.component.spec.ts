import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonaNaturalFormComponent } from './persona-natural-form.component';

describe('PersonaNaturalFormComponent', () => {
  let component: PersonaNaturalFormComponent;
  let fixture: ComponentFixture<PersonaNaturalFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PersonaNaturalFormComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PersonaNaturalFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
