from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from injector import inject
from metaverse.metaverse_service import MetaverseService
from entity.event import Event
from entity.media import Media
from dashboard.dashboard_service import DashboardService

Dashboard = Namespace('Dashboard')

@Dashboard.route("/statistics")
class DashboardEventList(Resource):
    @inject
    def __init__(self, dashboard_service:DashboardService, api):
        self._dashboard_service = dashboard_service
        super().__init__(api)

    def get(self):
        """광고 통계를 반환합니다."""

        return jsonify(self._dashboard_service.get_advertisement_statistics())