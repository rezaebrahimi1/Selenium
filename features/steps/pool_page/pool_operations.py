from behave import given, when, then, step, use_step_matcher
from page_classes.pool import PoolPage
from selenium.common.exceptions import NoSuchElementException
from base.exception import WarningException, ErrorException
from base.exceptions import NoSuchElementInDropdownList, OperationFailure  # ,NotEnoughDisk
from base import error_codes
use_step_matcher("re")
import time

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#                                                   Pool Creation
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
@given("The user is in Pool page")
def step_impl(context):
    context.pool_page = PoolPage(context.driver)
    assert context.pool_page.get_title() == 'Pool',\
        'The user is not in Pool page, user is in ' + context.pool_page.get_title() + ' page.'


@when('Click on "Create" button')
def step_impl(context):
    time.sleep(1)
    context.pool_page.click_create_btn()


@step('Enter Pool Name: "(.*?)"')
def step_impl(context, pool_name):
    context.pool_page.enter_pool_name(pool_name)

    assert context.pool_page.check_duplicate_name_warning() == False, \
        'Duplicate Pool name is not allowed, ' \
        'Pool with name "' + pool_name + '" already exists in Pool Configuration table.'


@step('Select Optimize Pool for: "(.*?)"')
def step_impl(context, optimize_for):
    try:
        context.pool_page.select_optimize_pool_for(optimize_for)
    except Exception:
        raise NoSuchElementInDropdownList('Optimized Pool for', 'Pool Creation',
                                          f" Element '{optimize_for}' does not exists in dropdown list",
                                          error_codes.ERROR_INVALID_OPTIMIZED_POOL_FOR)


@step('Select Recommended RAID Mode: "(.*?)"')
def step_impl(context, raid_mode):
    try:
        context.pool_page.select_raid_mode(raid_mode)
    except Exception:
        raise NoSuchElementInDropdownList('Recommended RAID Mode', 'Pool Creation',
                                          f" Element '{raid_mode}' does not exists in dropdown list",
                                          error_codes.ERROR_INVALID_RAID_MODE)
    context.pool_page.raid_mode = raid_mode


@step('Select Span Depth: "(.*?)"')
def step_impl(context, span_depth):
    """
    :param span_depth: Span Depth.
    :type context: behave.runner.Context
    """
    if context.pool_page.raid_mode in ("RAID10", "RAID5(50)", "RAID6(60)"):
        try:
            context.pool_page.select_span_depth(span_depth)
        except Exception:
            raise NoSuchElementInDropdownList('Span Depth', 'Pool Creation',
                                              f" Element '{span_depth}' does not exists in dropdown list",
                                              error_codes.ERROR_INVALID_SPAN_DEPTH)
    else:
        pass


@step('Select Stripe Size: "(.*?)"')
def step_impl(context, strp_size):
    """
    :param strp_size: Stripe Size.
    :type context: behave.runner.Context
    """
    try:
        context.pool_page.select_stripe_size(strp_size)
    except Exception:
        raise NoSuchElementInDropdownList('Stripe Size', 'Pool Creation',
                                          f" Element '{strp_size}' does not exists in dropdown list",
                                          error_codes.ERROR_INVALID_STRIPE_SIZE)


@step('Select Type of Disk Drive: "(.*?)"')
def step_impl(context, disk_type):
    try:
        context.pool_page.select_disk_type(disk_type)
    except Exception:
        raise NoSuchElementInDropdownList('Type of Disk Drive', 'Pool Creation',
                                          f" Element '{disk_type}' does not exists in dropdown list",
                                          error_codes.ERROR_INVALID_DISK_TYPE)


@step('Select Recommended Disk Number: "(.*?)"')
def step_impl(context, disk_num):
    try:
        context.pool_page.select_disk_number(disk_num)
    except Exception:
        raise NoSuchElementInDropdownList('Recommended Disk Number', 'Pool Creation',
                                          f" Element '{disk_num}' does not exists in dropdown list",
                                          error_codes.ERROR_INVALID_DISK_NUMBER)
    context.disk_num = int(disk_num)


@step('Select disks: "(.*?)"')
def step_impl(context, disk_selection):
    context.pool_page.disk_selection(context.disk_num, select_method='manually')


@step('Enable cache: "(.*?)"')
def step_impl(context, enable_cache):
    context.pool_page.cache_settings(enable_cache)


@step("Click on Create button in Pool Creation modal")
def step_impl(context):
    context.pool_page.click_create_pool_btn()
    try:
        context.pool_page.get_element(context.pool_page._error_message, locatortype='xpath')
    except NoSuchElementException:
        pass
    else:
        error_msg_text = context.pool_page.get_element(context.pool_page._error_message_text, locatortype='xpath').text
        raise OperationFailure('Pool Creation', 'An error occurred while creating a new Pool.\n' +
                               'User Interface Error Message:\n' + error_msg_text,
                               error_codes.ERROR_POOL_CREATION_FAILURE)


@then('Storage Pool "(.*?)" should be created successfully')
def step_impl(context, pool_name):
    context.pool_page.check_pool_existence(pool_name)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#                                                   Delete Pool
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
@when('Select desired Pool in Pool Configuration table: "(.*?)"')
def step_impl(context, pool_name):
    context.pool_page.select_desired_pool(pool_name)
    context.pool_name = pool_name


@step("Click on Delete button in Pool page")
def step_impl(context):
    context.pool_page.click_delete_btn()


@step("Press Delete button in confirmation message")
def step_impl(context):
    context.pool_page.confirm_delete_pool()
    try:
        context.pool_page.get_element(context.pool_page._error_message, locatortype='xpath')
    except NoSuchElementException:
        pass
    else:
        error_msg_text = context.pool_page.get_element(context.pool_page._error_message_text, locatortype='xpath').text
        raise OperationFailure('Pool Deletion', 'An error occurred while deleting the Pool.\n' +
                               'User Interface Error Message:\n' + error_msg_text,
                               error_codes.ERROR_POOL_DELETION_FAILURE)


@then('The Pool should be deleted successfully: "(.*?)"')
def step_impl(context, pool_name):
    context.pool_page.verify_pool_deletion(pool_name)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#                                                   Rename Pool
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
@step("Click on Rename button in Pool page")
def step_impl(context):
    context.pool_page.click_rename_btn()


@step('Enter new Pool name: "(.*?)"')
def step_impl(context, pool_name):
    context.pool_page.enter_pool_new_name(pool_name)


@step("Press Rename button")
def step_impl(context):
    context.pool_page.click_rename()
    try:
        context.pool_page.get_element(context.pool_page._error_message, locatortype='xpath')
    except NoSuchElementException:
        pass
    else:
        error_msg_text = context.pool_page.get_element(context.pool_page._error_message_text, locatortype='xpath').text
        raise OperationFailure('Pool Rename', 'An error occurred while renaming the Pool.\n' +
                               'User Interface Error Message:\n' + error_msg_text,
                               error_codes.ERROR_POOL_RENAME_FAILURE)


@then('Pool "(.*?)" should be renamed successfully to "(.*?)"')
def step_impl(context, pool_old_name, pool_new_name):
    context.pool_page.wait_for_element(
        context.pool_page._pool_configuration_table, locator_type='xpath', wait_method='visible')

    pool = '//div[@data-rows="pools"]//table//tbody//tr//td[2][text()="' + pool_old_name + '"]'
    assert context.pool_page.element_presence_check(pool, by_type='xpath') == False, \
        "Storage pool '" + pool_old_name + "' hasn't been renamed. " \
        "Pool with name '" + pool_old_name + "' exists in Pool Configuration table."

    pool = '//div[@data-rows="pools"]//table//tbody//tr//td[2][text()="' + pool_new_name + '"]'
    assert context.pool_page.element_presence_check(pool, by_type='xpath') == True, \
        "The storage Pool hasn't been renamed successfully to '" + pool_new_name + "'. " \
        "Pool with name '" + pool_new_name + "' is not shown in Pool Configuration table."

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#                                                    Pool Extension
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
@step("Click on Extend button in Pool page")
def step_impl(context):
    disk_num_before_extend = context.pool_page.get_element(
        '//table//td[2][text()="' + context.pool_name + '"]//following::td[3]', locatortype='xpath').text
    context.disk_num_before_extend = int(disk_num_before_extend)
    context.pool_page.click_extend_btn()


@step('Select Disk Number: "(.*?)" in Pool Extension modal')
def step_impl(context, disk_num):
    try:
        context.pool_page.select_disk_number(disk_num)
    except:
        raise NoSuchElementInDropdownList('Recommended Disk Number', 'Pool Extension',
                                          f" Element '{disk_num}' does not exists in dropdown list",
                                          error_codes.ERROR_INVALID_DISK_NUMBER)

    context.pool_page.check_disk_warning_pool_extension()
    context.disk_num = int(disk_num)



@step("Click on Extend button in Pool Extension modal")
def step_impl(context):
    context.pool_page.click_extend_pool_btn()
    try:
        context.pool_page.get_element(context.pool_page._error_message, locatortype='xpath')
    except NoSuchElementException:
        pass
    else:
        error_msg_text = context.pool_page.get_element(context.pool_page._error_message_text, locatortype='xpath').text
        raise OperationFailure('Pool Extension', 'An error occurred while extending the Pool.\n' +
                               'User Interface Error Message:\n' + error_msg_text,
                               error_codes.ERROR_POOL_EXTENSION_FAILURE)


@then('Number of disks should be shown correctly in Pool Configuration table for pool: "(.*?)"')
def step_impl(context, pool_name):
    number_of_disks = int(context.pool_page.get_element(
        '//table//td[2][text()="' + pool_name + '"]//following::td[3]', locatortype='xpath').text)

    assert number_of_disks == (context.disk_num + context.disk_num_before_extend), \
        "The storage Pool hasn't been extended successfully. " \
        "Number of disks is not shown correctly in Pool Configuration table."