from django.urls import path
from . import views

urlpatterns = [
    path('new-user/', views.register_user_step, name="new-user"),
    path('new-person/', views.register_person_step, name="new-person"),
    path('new-person-type/', views.register_person_type_step, name="new-person-type"),
    path('login/', views.loginHandler, name="login"),
    path('logout/', views.logoutHandler, name="logout"),
    path('alterar-senha/', views.newPassword, name="alterar-senha"),
    path('area-do-usuario/', views.userArea, name="area-do-usuario"),
    path('success/', views.paymentSuccess, name="payment-success"),
    path('failure/', views.paymentFailure, name="payment-failure"),
    path('pendings/', views.paymentPendings, name="payment-pendings"),
    path('send-work/', views.updateWork, name='send-work'),
    path('subscription/', views.subscriptions, name='subscription'),
    path('subscriptions_combo/', views.subscriptions_combo, name='subscriptions_combo'),
    path('subscription-success/', views.updateSuccessPaidSubscription, name="subscription-success"),
    path('subscription-failed/', views.updateFailedPaidSubscription, name="subscription-failed"),
    path('payment-subscription-success/', views.updatePaymentSubscriptionSuccess, name="payment-subscription-success"),
    path('payment-subscription-success/', views.updatePaymentSubscriptionComboSuccess, name="payment-subscription-combo-success"),
    path('combo/', views.getCPF, name='combo'),
    path('check-cpf/', views.check_cpf, name='check-cpf'),
]
