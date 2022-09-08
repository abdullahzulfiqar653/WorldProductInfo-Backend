from django.db.models import Q
from core.models import Category


def all_categories_have_no_childs(category_id):
    all_parent_category_ids = Category.objects.values("parentcategoryid")
    categories_have_no_childs = []
    category_ids_to_get_childs = []
    category_ids_to_get_childs.append(category_id)
    # getting categoryIds by using parentCategoryId from the category table.
    while True:
        category_ids = Category.objects.filter(
            parentcategoryid__in=category_ids_to_get_childs)

        categories_have_childs = category_ids.filter(
            categoryid__in=all_parent_category_ids)

        categories_have_no_childs.extend(category_ids.filter(
            ~Q(categoryid__in=categories_have_childs.values(
                "categoryid"))).values_list("categoryid", flat=True))

        category_ids_to_get_childs = categories_have_childs.values(
            "categoryid")

        if not categories_have_childs:
            break
    return categories_have_no_childs


def categories_with_all_childs(category_id):
    all_parent_category_ids = Category.objects.select_related("categoryid").values(
        "parentcategoryid")
    all_childs_of_requested_category = []
    category_ids_to_get_childs = []
    category_ids_to_get_childs.append(category_id)
    all_childs_of_requested_category.append(category_id)
    # getting categoryIds by using parentCategoryId from the category table.
    while True:
        category_ids = Category.objects.filter(
            parentcategoryid__in=category_ids_to_get_childs).values('categoryid')
        categories_have_childs = category_ids.filter(
            categoryid__in=all_parent_category_ids).values('categoryid')

        all_childs_of_requested_category.extend(
            category_ids.values_list("categoryid", flat=True))

        category_ids_to_get_childs = categories_have_childs.values(
            "categoryid")

        if not categories_have_childs:
            break

    return all_childs_of_requested_category
