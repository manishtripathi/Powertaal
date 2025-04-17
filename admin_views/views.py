from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
import subprocess
import os

# Uncomment the decorator to restrict access to staff members only
# @staff_member_required
def github_backup(request):
    """
    View for the GitHub backup page.
    """
    return render(request, 'admin/github_backup.html') 