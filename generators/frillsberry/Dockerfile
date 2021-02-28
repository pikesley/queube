FROM ruby:3

ENV PROJECT frillsberry
ENV APP_HOME /opt/${PROJECT}

RUN gem update bundler

COPY ./gems.* ${APP_HOME}/
RUN cd ${APP_HOME} && \
    bundle install

COPY ./ ${APP_HOME}

WORKDIR ${APP_HOME}
CMD ["ruby", "frillsberry.rb"]
