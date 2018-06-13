from contextlib import contextmanager

from fabsetup.fabutils import print_msg, run, subtask, suggest_localhost, task
from utlz import flo

from fabsetup_theno_letsencrypt.fabutils import checkup_git_repo
from fabsetup_theno_letsencrypt.fabutils import checkup_git_repos
from fabsetup_theno_letsencrypt.fabutils import install_file
from fabsetup_theno_letsencrypt.fabutils import install_user_command
from fabsetup_theno_letsencrypt._version import __version__


@contextmanager
def stopped_nginx():
    print_msg('\n## stop nginx\n')
    run('sudo service nginx stop')
    try:
        yield
    finally:
        print_msg('\n## start nginx\n')
        run('sudo service nginx start')


@subtask
def list_cert_files():
    run('sudo tree /etc/letsencrypt')


@task
@suggest_localhost
def letsencrypt():
    '''Create tls-webserver certificates which are trusted by the web pki.

    The wildcard certificates are issued by Let's Encrypt.

    Touched files, dirs, and installed packages:

        /etc/letsencrypt/*
    '''

    repo_dir = checkup_git_repo('https://github.com/certbot/certbot.git',
                                prefix='## ', postfix='\n')

    with stopped_nginx():

        options = ' '.join([
            '--standalone',
            '--rsa-key-size 4096',
        ])

        from config import domain_groups

        for domains in domain_groups:

            domains_str = ', '.join(domains)
            print_msg(flo(
                '\n## Create certificate for: {domains_str}\n'))

            domain_opts = ' '.join([flo(' -d {domain}') for domain in domains])
            # command 'letsencrypt-auto' requests for root by itself via 'sudo'
            run(flo('{repo_dir}/letsencrypt-auto  '
                    '{options} {domain_opts}  certonly'))

    list_cert_files()
