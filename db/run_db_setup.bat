@echo off
psql -U postgres -d book_manager -f db_setup.sql
pause
