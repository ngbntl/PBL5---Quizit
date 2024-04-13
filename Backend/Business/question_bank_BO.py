from Backend.DataAccess.collection_DA import collection_DA
from Backend.DataAccess.question_bank_DA import question_bank_DA


class question_bank_BO:

    # INSERT
    def insert_question_bank(self, teacher_id: str, collection_id: str, name: str) -> str:
        if collection_id is None:
            raise Exception("collection_id is required")
        collection_service = collection_DA()
        question_bank_service = question_bank_DA()
        if collection_service.check_owner(collection_id, teacher_id) is False:
            raise Exception(f"teacher {teacher_id} is not the owner of collection {collection_id}")
        return question_bank_service.insert_question_bank(collection_id, name)

    # SELECT
    def get_question_banks_by_collection(self, teacher_id: str, collection_id: str) -> list[dict]:
        collection_service = collection_DA()
        question_bank_service = question_bank_DA()
        if collection_service.check_owner(collection_id, teacher_id) is False:
            raise Exception(f"teacher {teacher_id} is not the owner of collection {collection_id}")
        return question_bank_service.get_question_banks_by_collection(collection_id)

    # UPDATE
    def update_question_bank(self, teacher_id, question_bank_id, name):
        collection_service = collection_DA()
        question_bank_service = question_bank_DA()
        if collection_service.check_owner(question_bank_service.get_collection_id(question_bank_id),
                                          teacher_id) is False:
            raise Exception(f"teacher {teacher_id} is not the owner of question bank {question_bank_id}")
        question_bank_service.update_name(question_bank_id=question_bank_id, name=name)
