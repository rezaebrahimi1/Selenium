from behave import given, when, then, step, use_step_matcher
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from page_classes.go_to_page import GoToPage
use_step_matcher("re")
import base.custom_logger as cl
import logging

# ================================================ Go to Pool page =====================================================
@given("The user Logged into User Interface")
def step_impl(context):
    context.GoToPage = GoToPage(context.driver)
    pass


@when('Click on "Storage" from side-menu')
def step_impl(context):
    context.GoToPage.click_storage_menu()


@step('Click on "Pool" from Storage sub-menu')
def step_impl(context):
    context.GoToPage.click_pool_link()


@then("The user is in Pool page")
def step_impl(context):
    # log = cl.custom_logger(logging.DEBUG)
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     log.info('An error occurred while loading Pool page.')
    #     raise AssertionError('An error occurred while loading Pool page.')
    pass

# ================================================ Go to LUN page ======================================================
@step('Click on "LUN" from Storage sub-menu')
def step_impl(context):
    context.GoToPage.click_lun_link()


@then("The user is in LUN page")
def step_impl(context):
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading LUN page.')
    pass

# ============================================= Go to RapidStore page ==================================================
@step('Click on "RapidStore" from Storage sub-menu')
def step_impl(context):
    time.sleep(1)
    context.GoToPage.click_rapidstore_link()


@then("The user is in RapidStore page")
def step_impl(context):
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading RapidStore page.')
    pass

# ============================================= Go to HotSpare page ====================================================
@step('Click on "HotSpare" from Storage sub-menu')
def step_impl(context):
    context.GoToPage.click_hotspare_link()


@then("The user is in HotSpare page")
def step_impl(context):
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading HotSpare page \n' +
    #                          context.browser.find_element_by_xpath('//div[@class="modal-body"]').text)
    pass

# ============================================ Go to Host Info page ====================================================
@when('Click on "Host List" from side-menu')
def step_impl(context):
    context.GoToPage.click_host_list_menu()


@step('Click on "Host Info" from "Host List" sub-menu')
def step_impl(context):
    context.GoToPage.click_host_info_link()


@then('The user is in "Host Info" page')
def step_impl(context):
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError("An error occurred while loading 'Host Info' page")
    pass

# ========================================== Go to Access Control page =================================================
@step('Click on "Access Control" from "Host List" sub-menu')
def step_impl(context):
    context.GoToPage.click_access_control_link()


@then('The user is in "Access Control" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError("An error occurred while loading 'Host Info' page")
    pass

# ========================================== Go to iSCSI and CHAP page =================================================
@step('Click on "iSCSI and CHAP" from "Host List" sub-menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.GoToPage.click_iscsi_and_chap_link()


@then('The user is in "iSCSI and CHAP" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading "iSCSI and CHAP" page \n' +
    #                          context.browser.find_element_by_xpath('//div[@class="modal-body"]').text)
    pass

# ========================================== Go to FileSystem page =====================================================
@when('Click on "NAS" from side-menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.GoToPage.click_nas_menu()


@step('Click on "Filesystems" from "NAS" sub-menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.GoToPage.click_filesystem_link()


@then('The user is in "Filesystem" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading "iSCSI and CHAP" page \n' +
    #                          context.browser.find_element_by_xpath('//div[@class="modal-body"]').text)
    pass

# ========================================== Go to NAS Server page =====================================================
@step('Click on "NAS Servers" from "NAS" sub-menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.GoToPage.click_nas_servers_link()


@then('The user is in "NAS Server" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading "NAS Access" page \n' +
    #                          context.browser.find_element_by_xpath('//div[@class="modal-body"]').text)
    pass

# ========================================== Go to NAS Access page =====================================================
@step('Click on "NAS Accesses" from "NAS" sub-menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.GoToPage.click_nas_accesses_link()


@then('The user is in "NAS Access" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading "NAS Access" page \n' +
    #                          context.browser.find_element_by_xpath('//div[@class="modal-body"]').text)
    pass

# =========================================== Go to SMB Share page =====================================================
@step('Click on "SMB Shares" from "NAS" sub-menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.GoToPage.click_smb_share_link()


@then('The user is in "SMB Share" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading "SMB Share" page \n' +
    #                          context.browser.find_element_by_xpath('//div[@class="modal-body"]').text)
    pass

# =========================================== Go to NFS Share page =====================================================
@step('Click on "NFS Shares" from "NAS" sub-menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.GoToPage.click_nfs_share_link()


@then('The user is in "NFS Share" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading "NFS Share" page \n' +
    #                          context.browser.find_element_by_xpath('//div[@class="modal-body"]').text)
    pass
# ============================================ Go to Snapshot page =====================================================
@when('Click on "Protection" from side-menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.GoToPage.click_protection_menu()


@step('Click on "Snapshot" from "Protection" sub-menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.GoToPage.click_snapshot_link()


@then('The user is in "Snapshot" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # try:
    #     context.browser.find_element_by_id('alert')
    # except NoSuchElementException:
    #     pass
    # else:
    #     raise AssertionError('An error occurred while loading "Snapshot" page \n' +
    #                          context.browser.find_element_by_xpath('//div[@class="modal-body"]').text)
    pass