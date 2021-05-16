# import unittest
# from src import db
# from tests.test_base import BasicTestCase
# from src.services.department import DepartmentService
# from src.models.models import Department
#
#
# class DepartmentTestCase(BasicTestCase):
#     def test_dep_is_added(self):
#         test_department = Department('test_dep', 'test_descr')
#         DepartmentService.save_to_db(test_department)
#         self.assertEqual(db.session.query(Department).filter_by(name='test_dep').first().description, 'test_descr')
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
