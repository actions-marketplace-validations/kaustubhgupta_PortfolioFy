from utils.adders import Adder

adder = Adder()


def genHTMLLevel1(user_data, project_repos, hackathon_repos, blogs, stats_choice, social_links, resume_link, allow_footer):

    template = f'''
    <html>
    <title>{user_data['name']} Portfolio</title>
    <head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <link href="https://www.kaustubhgupta.me/themescss/level1.css" rel="stylesheet" />
    </head>
    <body>
    <div class="div-main" align="center">
    <img class="img-rounded" alt="Image" height="350px" src="{user_data['git_photo_url']}" />
    <h1 style='color:#f24b4b'> Hi, I am <a href="https://github.com/{user_data['username']}">{user_data['name']}</a>👨‍🎓 </h1>
    <h2 style='color:#21439e'>{user_data['git_bio']}</h2>
    <!-- RESUME-ENTRY -->
    <!-- GITHUBSTATS-ENTRY -->
    <h3 style='color:#751878'>Followers: <b>{user_data['git_followers']}</b>, Following: <b>{user_data['git_following']}</b></h3>
    {social_links}
    <br>
    <h1 style="color:#d45131"> My Projects👇</h1>
    <text class="text-info">*Updated: {user_data["latest_updated"]}</text>
    <br>
    {project_repos}
    <br>
    <!-- HACKATHON-ENTRY -->
    <br>
    <!-- BLOG-ENTRY -->
    <h3 style="color:#9a08c7">Contact on Email: {user_data['git_email']}</h3>
    </div>
    <div class="footer">
    <!-- FOOTER-ENTRY -->
    </div>
    </body>
    </html>
    '''
    if stats_choice == '1':
        statsImg = f'''<img class="img-stats" src="https://github-readme-stats.vercel.app/api?username={user_data['username']}&show_icons=true&theme=radical&count_private=true">'''
        template = template.replace('<!-- GITHUBSTATS-ENTRY -->', statsImg)

    elif stats_choice == '2':
        statsImg = f'''<img src="https://metrics.lecoq.io/{user_data['username']}?followup=1&isocalendar=1">'''
        template = template.replace('<!-- GITHUBSTATS-ENTRY -->', statsImg)

    if blogs:
        template = adder.addBlogsL1(template)

    if 'false' not in resume_link:
        template = adder.addResumeL2(template, resume_link)

    if allow_footer:
        template = adder.addFooter(template)

    if hackathon_repos is not None:
        retunFile = adder.addHackathonL1(
            hackathon_repos, user_data["latest_updated"], template)
        return retunFile
    else:
        return template
