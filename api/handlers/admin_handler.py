from api.dao.admin_dao import AdminDAO
from api.dao.user_dao import UserDAO
from api.handlers.error_handler import ErrorHandler
from flask import jsonify


class AdminHandler(object):
    def build_admin_dict(self, row):
        admin_dict = {}
        admin_dict["admin_id"] = row[0]
        admin_dict["admin_name"] = row[1]
        return admin_dict

    def get_all_admins(self):
        result = AdminDAO().get_all_admins()
        return jsonify(admin=result), 200

    def get_admin_by_id(self, user_id):
        result = AdminDAO().get_admin_by_id(user_id)
        if not result:
            return ErrorHandler().not_found()
        else:
            return jsonify(admin=result), 200

    def insert_admin(self, admin):
        admin_dao = AdminDAO()
        user_dao = UserDAO()

        try:
            admin_name = admin["admin_name"]
            username = admin["username"]
            password = admin["password"]
            phone_number = admin["phone_number"]
        except KeyError:
            ErrorHandler().bad_request()

        user_id = user_dao.insert_user(username, password, phone_number)
        admin_id = admin_dao.insert_admin(admin_name, user_id)

        return (self.build_admin_dict(
                 (
                    admin_id,
                    admin_name,
                    user_id,
                 )
            ), 201,
        )


    def update_admin(self, admin_id, admin):
        if not self.get_admin_by_id(admin_id):
            return ErrorHandler().not_found()

        try:
            admin_name = admin["admin_name"]

        except KeyError:
            ErrorHandler().bad_request()

            if admin_name:
                AdminDAO().update_admin(admin_id, admin_name)

                return (self.build_admin_dict((admin_id, admin_name)), 200)
            else:
                return ErrorHandler().bad_request()
        else:
            return ErrorHandler().bad_request()

    def delete_admin(self, admin_id):
        if not self.get_admin_by_id(admin_id):
            return ErrorHandler().not_found()
        else:
            AdminDAO().delete_admin(admin_id)
            return jsonify(Deletion="OK"), 200
