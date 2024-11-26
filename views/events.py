from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import db, Evento

events_bp = Blueprint('events', __name__)

@events_bp.route('/dashboard')
def dashboard():
    # Mostrar lista de eventos del usuario logueado
    pass

@events_bp.route('/event/new', methods=['GET', 'POST'])
def new_event():
    # Crear nuevo evento
    pass

@events_bp.route('/event/<int:id>')
def view_event(id):
    # Mostrar detalles del evento
    pass

@events_bp.route('/event/edit/<int:id>', methods=['GET', 'POST'])
def edit_event(id):
    # Editar evento existente
    pass
